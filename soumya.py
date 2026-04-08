import asyncio
import os
from datetime import datetime
import openai

from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType
from graphiti_core.llm_client.openai_client import OpenAIClient, LLMConfig
from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig

os.environ["OPENAI_API_KEY"] = "ollama"
os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1"

llm = OpenAIClient(
    config=LLMConfig(
        model="mistral",
        temperature=0
    )
)

embedder = OpenAIEmbedder(
    config=OpenAIEmbedderConfig(
        model="nomic-embed-text",
    )
)

embedder = OpenAIEmbedder(
    config=OpenAIEmbedderConfig(
        api_key="ollama",
        base_url="http://localhost:11434/v1",
        embedding_model="nomic-embed-text"
    )
)


graphiti = Graphiti(
    uri="bolt://localhost:7687",
    user="neo4j",
    password="neo4j123",
    llm_client=llm,
    embedder=embedder
)

async def main():
    print("🔧 Building indices...")
    await graphiti.build_indices_and_constraints()
    print("✅ Ready!")

    print("📥 Adding episode...")
    await graphiti.add_episode(
        name="Test Episode",
        episode_body="Dealer A and Dealer B are suspicious in Karnataka.",
        source=EpisodeType.text,
        reference_time=datetime.now(),
        source_description="Test case",
        group_id="CASE-1"
    )
    print("✅ Episode added!")

    print("\n🔍 Searching...")
    results = await graphiti.search(query="suspicious dealers", num_results=3)

    print("\n📊 Results:")
    for r in results:
        print("-", r.fact)

    await graphiti.close()

asyncio.run(main())