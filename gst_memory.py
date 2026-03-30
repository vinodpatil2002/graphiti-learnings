import asyncio
import os
from datetime import datetime
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType
from graphiti_core.llm_client.openai_client import OpenAIClient, LLMConfig
from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig
from dotenv import load_dotenv


load_dotenv()


# ── CONFIG ──────────────────────────────────────
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")

os.environ["OPENAI_API_KEY"] = OLLAMA_API_KEY
os.environ["OPENAI_BASE_URL"] = OLLAMA_BASE_URL

# ── SETUP ────────────────────────────────────────
llm_client = OpenAIClient(
    config=LLMConfig(
        api_key=OLLAMA_API_KEY,
        model="mistral",
        base_url=OLLAMA_BASE_URL
    )
)

embedder = OpenAIEmbedder(
    config=OpenAIEmbedderConfig(
        api_key=OLLAMA_API_KEY,
        embedding_model="nomic-embed-text",
        base_url=OLLAMA_BASE_URL
    )
)

graphiti = Graphiti(
    uri=NEO4J_URI,
    user=NEO4J_USER,
    password=NEO4J_PASSWORD,
    llm_client=llm_client,
    embedder=embedder
)

# ── MAIN ─────────────────────────────────────────
async def main():

    print("Building indices...")
    await graphiti.build_indices_and_constraints()
    print("Ready!")

    print("Adding Episode 1...")
    await graphiti.add_episode(
        name="Case-001 Initial Investigation",
        episode_body="""
        On March 15 2024, investigator Priya Sharma flagged Dealer F
        (GSTIN: 36FFFF1111F1Z1) from Telangana. Dealer F filed 6 invoices
        in March 2024 totalling Rs 5.7 lakh, all under HSN code 8471 (Computers).
        Dealer F has a SIMILAR_TO score of 0.96 with Dealer G and 0.92 with
        Dealer K, forming a suspicious circular cluster of 6 dealers.
        Invoice amounts range from Rs 94500 to Rs 95200 suggesting
        coordinated fake billing.
        """,
        source=EpisodeType.text,
        reference_time=datetime(2024, 3, 15),
        source_description="GST fraud investigation note",
        group_id="CASE-001"
    )
    print("Episode 1 added!")

    print("Adding Episode 2...")
    await graphiti.add_episode(
        name="Case-001 Follow Up",
        episode_body="""
        On March 22 2024, investigator Priya Sharma found that Dealer G
        (GSTIN: 36GGGG2222G2Z2) is also linked to Dealer H and Dealer I.
        All three dealers registered on the same date: January 5 2023.
        Same registration date across multiple dealers in a fraud cluster
        is a strong ghost dealer signal. Dealer G filed 4 invoices in
        March 2024 under HSN code 8471 totalling Rs 3.8 lakh.
        """,
        source=EpisodeType.text,
        reference_time=datetime(2024, 3, 22),
        source_description="GST fraud investigation note",
        group_id="CASE-001"
    )
    print("Episode 2 added!")

    print("Adding Episode 3...")
    await graphiti.add_episode(
        name="Case-002 New Suspect",
        episode_body="""
        On March 28 2024, investigator Rahul Mehta opened Case 002.
        A new dealer XYZ Supplies (GSTIN: 36XYZZ9999X9Z9) from Telangana
        was flagged for velocity spike — filed 2 invoices in January 2024
        but 18 invoices in March 2024. XYZ Supplies also shares HSN code
        8471 with the Case 001 cluster suggesting possible connection
        to Dealer F and Dealer G.
        """,
        source=EpisodeType.text,
        reference_time=datetime(2024, 3, 28),
        source_description="GST fraud investigation note",
        group_id="CASE-002"
    )
    print("Episode 3 added!")

    print("\nSearching memory...")
    results = await graphiti.search(
        query="Which dealers are suspicious in Telangana?",
        num_results=5
    )

    print("\n── SEARCH RESULTS ──────────────────")
    for r in results:
        print(r.fact)
        print("---")

    await graphiti.close()

asyncio.run(main())