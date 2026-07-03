import os
import re
from io import BytesIO
import time
from typing import Any

import pandas as pd
import requests
import streamlit as st


st.set_page_config(
    page_title="Pinecone Semantic Search",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


SAMPLE_NOTES_URL = (
    "https://raw.githubusercontent.com/pinecone-io/examples/main/docs/data/"
    "sample_notes_data.jsonl"
)
DEFAULT_INDEX_NAME = "agent-ai"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
RERANK_MODEL = "bge-reranker-v2-m3"
FALLBACK_MEDICAL_NOTES = [
    {
        "id": "LOCAL001",
        "metadata": {
            "symptoms": "chest pain, shortness of breath",
            "tests": "EKG, troponin blood test",
            "advice": "seek urgent medical evaluation",
        },
    },
    {
        "id": "LOCAL002",
        "metadata": {
            "symptoms": "fever, cough, fatigue",
            "tests": "temperature check, respiratory exam",
            "advice": "hydrate, rest, monitor breathing",
        },
    },
    {
        "id": "LOCAL003",
        "metadata": {
            "symptoms": "headache, nausea, light sensitivity",
            "tests": "neurological exam",
            "advice": "avoid triggers and consult a clinician if severe",
        },
    },
    {
        "id": "LOCAL004",
        "metadata": {
            "condition": "diabetes",
            "symptoms": "increased thirst, frequent urination",
            "tests": "HbA1c, fasting glucose",
            "medications": "metformin discussion with physician",
        },
    },
    {
        "id": "LOCAL005",
        "metadata": {
            "symptoms": "abdominal pain, vomiting",
            "tests": "physical exam, hydration status",
            "advice": "avoid self-medication and seek care if persistent",
        },
    },
    {
        "id": "LOCAL006",
        "metadata": {
            "symptoms": "joint pain, swelling",
            "tests": "inflammation markers, joint exam",
            "advice": "rest joint and discuss anti-inflammatory options",
        },
    },
    {
        "id": "LOCAL007",
        "metadata": {
            "symptoms": "anxiety, insomnia, palpitations",
            "tests": "thyroid check, mental health screening",
            "advice": "breathing exercises and professional follow-up",
        },
    },
    {
        "id": "LOCAL008",
        "metadata": {
            "symptoms": "back pain after lifting",
            "tests": "mobility exam, red flag screening",
            "advice": "gentle movement and medical care if weakness occurs",
        },
    },
]


def inject_css() -> None:
    st.markdown(
        """
        <style>
        :root {
            --surface: #ffffff;
            --surface-soft: #f6f8fb;
            --ink: #132033;
            --muted: #667085;
            --line: #d8dee8;
            --accent: #0f766e;
            --accent-2: #2563eb;
            --warn: #b45309;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(15, 118, 110, .10), transparent 30rem),
                linear-gradient(180deg, #f7fafc 0%, #eef3f8 100%);
            color: var(--ink);
        }

        [data-testid="stSidebar"] {
            background: #101828;
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] small {
            color: #eef4ff;
        }

        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea {
            background: #ffffff;
            color: #111827;
            border: 1px solid #cbd5e1;
            caret-color: #0f766e;
        }

        [data-testid="stTextInput"] input::placeholder,
        [data-testid="stTextArea"] textarea::placeholder {
            color: #64748b;
            opacity: 1;
        }

        [data-testid="stSidebar"] [data-testid="stTextInput"] input {
            background: #ffffff;
            color: #111827;
        }

        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1240px;
        }

        .hero {
            padding: 1.4rem 0 1rem;
            border-bottom: 1px solid rgba(19, 32, 51, .10);
            margin-bottom: 1.2rem;
        }

        .hero h1 {
            font-size: clamp(2rem, 4vw, 3.5rem);
            line-height: 1;
            margin: 0 0 .75rem;
            letter-spacing: 0;
        }

        .hero p {
            color: var(--muted);
            font-size: 1.05rem;
            max-width: 780px;
            margin: 0;
        }

        .metric-card {
            background: rgba(255, 255, 255, .82);
            border: 1px solid rgba(19, 32, 51, .10);
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 12px 30px rgba(16, 24, 40, .06);
            min-height: 104px;
        }

        .metric-card span {
            color: var(--muted);
            font-size: .82rem;
            text-transform: uppercase;
            letter-spacing: .04em;
        }

        .metric-card strong {
            display: block;
            color: var(--ink);
            font-size: 1.55rem;
            margin-top: .35rem;
        }

        .result-card {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1rem 1.1rem;
            margin: .65rem 0;
            box-shadow: 0 10px 24px rgba(16, 24, 40, .045);
        }

        .result-card h4 {
            margin: 0 0 .45rem;
            font-size: 1rem;
        }

        .score {
            display: inline-flex;
            align-items: center;
            gap: .4rem;
            background: #ecfdf3;
            color: #05603a;
            border: 1px solid #abefc6;
            border-radius: 999px;
            padding: .18rem .58rem;
            font-size: .82rem;
            font-weight: 700;
        }

        .hint {
            color: var(--muted);
            font-size: .92rem;
        }

        .warning-box {
            border-left: 4px solid var(--warn);
            background: #fffbeb;
            padding: .8rem 1rem;
            border-radius: 6px;
            color: #78350f;
            margin: .8rem 0;
        }

        div[data-testid="stTabs"] button {
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_pinecone_api_key(manual_key: str | None = None) -> str | None:
    try:
        secret_key = st.secrets.get("PINECONE_API_KEY")
    except Exception:
        secret_key = None
    return (manual_key or "").strip() or secret_key or os.getenv("PINECONE_API_KEY")


def clean_pinecone_api_key(raw_key: str) -> str:
    key = str(raw_key or "").strip().strip("\"'")
    match = re.search(r"pcsk_[A-Za-z0-9_-]+", key)
    if match:
        return match.group(0)
    return key


def validate_pinecone_api_key(raw_key: str) -> tuple[str, str | None]:
    key = clean_pinecone_api_key(raw_key)
    if not key:
        return "", "Cle Pinecone introuvable."

    try:
        key.encode("ascii")
    except UnicodeEncodeError:
        return "", (
            "La cle Pinecone contient un caractere non valide. "
            "Colle uniquement la valeur qui commence par `pcsk_`, sans texte autour."
        )

    if not key.startswith("pcsk_"):
        return "", "La cle Pinecone doit commencer par `pcsk_`."

    return key, None


@st.cache_resource(show_spinner=False)
def get_pinecone_client(api_key: str):
    from pinecone import Pinecone

    return Pinecone(api_key=api_key)


@st.cache_resource(show_spinner="Chargement du modèle d'embedding...")
def load_embedding_model():
    import torch
    from transformers import AutoModel, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL)
    model = AutoModel.from_pretrained(EMBEDDING_MODEL)
    model.eval()
    return tokenizer, model, torch


@st.cache_data(show_spinner="Téléchargement des notes médicales...")
def load_sample_notes() -> tuple[pd.DataFrame, str]:
    try:
        session = requests.Session()
        session.trust_env = False
        response = session.get(SAMPLE_NOTES_URL, timeout=30)
        response.raise_for_status()
        df = pd.read_json(BytesIO(response.content), orient="records", lines=True)
        return df, "Dataset GitHub Pinecone"
    except Exception:
        return pd.DataFrame(FALLBACK_MEDICAL_NOTES), "Dataset local de secours"


def get_embedding(question: str) -> list[float]:
    tokenizer, model, torch = load_embedding_model()
    encoded_input = tokenizer(
        question,
        padding=True,
        truncation=True,
        return_tensors="pt",
    )

    with torch.no_grad():
        output = model(**encoded_input)
        attention_mask = encoded_input["attention_mask"].unsqueeze(-1)
        masked_output = output.last_hidden_state * attention_mask
        summed = masked_output.sum(dim=1)
        counts = attention_mask.sum(dim=1).clamp(min=1)
        embedding = summed / counts

    return embedding[0].tolist()


def metadata_to_text(metadata: dict[str, Any]) -> str:
    return "; ".join(f"{key}: {value}" for key, value in metadata.items())


def prepare_notes_for_upsert(df: pd.DataFrame) -> pd.DataFrame:
    if "values" in df.columns:
        return df

    prepared = df.copy()
    prepared["values"] = [
        get_embedding(metadata_to_text(metadata or {}))
        for metadata in prepared["metadata"]
    ]
    return prepared[["id", "values", "metadata"]]


def normalize_match(match: Any) -> dict[str, Any]:
    if isinstance(match, dict):
        return match
    return {
        "id": getattr(match, "id", ""),
        "score": getattr(match, "score", 0),
        "metadata": getattr(match, "metadata", {}),
    }


def score_as_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def render_metric_cards(items: list[tuple[str, str]]) -> None:
    columns = st.columns(len(items))
    for column, (label, value) in zip(columns, items):
        column.markdown(
            f"""
            <div class="metric-card">
                <span>{label}</span>
                <strong>{value}</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_result_card(rank: int, score: float, title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="result-card">
            <h4>#{rank} · {title}</h4>
            <div class="score">Score {score:.4f}</div>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def ensure_index(pc, index_name: str, cloud: str, region: str):
    from pinecone import ServerlessSpec

    if not pc.has_index(name=index_name):
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud=cloud, region=region),
        )

    return pc.Index(name=index_name)


def wait_until_fresh(index, expected_count: int, timeout_seconds: int = 90) -> int:
    deadline = time.time() + timeout_seconds
    latest_count = 0
    while time.time() < deadline:
        stats = index.describe_index_stats()
        latest_count = int(getattr(stats, "total_vector_count", 0))
        if latest_count >= expected_count:
            return latest_count
        time.sleep(3)
    return latest_count


def apple_reranking_tab(pc) -> None:
    st.subheader("Reranking de documents")
    st.caption("Démo inspirée de la première partie du notebook : retrouver les textes les plus proches d'une requête.")

    default_documents = [
        "Les pommes sont des fruits croquants et sucrés qui poussent sur les arbres. Il en existe de nombreuses variétés comme la Gala, la Fuji et la Granny Smith.",
        "Apple Inc. conçoit, fabrique et commercialise des smartphones, des ordinateurs personnels, des tablettes, des objets connectés et des accessoires dans le monde entier. Ses produits les plus célèbres sont l'iPhone, le Mac, l'iPad et l'Apple Watch.",
        "Une pomme mûre se mange souvent crue, mais elle peut aussi être utilisée dans les tartes, les compotes et les cidres. Elle est une bonne source de fibres et de vitamine C.",
        "L'App Store d'Apple propose des millions d'applications pour ses appareils, offrant un vaste écosystème de logiciels et de services.",
        "Parmi les services Apple populaires, on trouve Apple Music, Apple TV+, Apple Arcade et iCloud, qui proposent des abonnements pour le divertissement et le stockage dans le nuage.",
    ]

    left, right = st.columns([0.42, 0.58], gap="large")
    with left:
        query = st.text_input("Requête", value="Écosystème Apple")
        top_n = st.slider("Nombre de résultats", 1, len(default_documents), 3)
        edited = st.text_area(
            "Documents à classer",
            value="\n\n".join(default_documents),
            height=330,
            help="Sépare les documents par une ligne vide.",
        )
        run = st.button("Lancer le reranking", type="primary", use_container_width=True)

    with right:
        documents = [doc.strip() for doc in edited.split("\n\n") if doc.strip()]
        render_metric_cards(
            [
                ("Modèle", RERANK_MODEL),
                ("Documents", str(len(documents))),
                ("Top N", str(top_n)),
            ]
        )

        if run:
            if not query.strip() or not documents:
                st.warning("Ajoute une requête et au moins un document.")
                return

            with st.spinner("Classement en cours avec Pinecone..."):
                reranked = pc.inference.rerank(
                    model=RERANK_MODEL,
                    query=query,
                    documents=[
                        {"id": str(index), "text": document}
                        for index, document in enumerate(documents)
                    ],
                    top_n=top_n,
                    return_documents=True,
                )

            for rank, match in enumerate(reranked.data, start=1):
                document = getattr(match, "document", {}) or {}
                text = document.get("text", "")
                render_result_card(rank, score_as_float(match.score), "Document retenu", text)
        else:
            st.info("Configure la requête puis lance le classement.")


def medical_search_tab(pc, index_name: str, cloud: str, region: str) -> None:
    st.subheader("Recherche sémantique sur notes médicales")
    st.caption("Création d'un index serverless, ingestion du dataset JSONL, recherche vectorielle puis reranking.")

    df, dataset_source = load_sample_notes()

    controls, results_area = st.columns([0.36, 0.64], gap="large")
    with controls:
        question = st.text_area(
            "Question médicale",
            value="I'm very sick, what treatment can I take?",
            height=105,
        )
        refined_query = st.text_input("Question affinée pour le reranking", value="My heart is weak")
        top_k = st.slider("Résultats de recherche", 1, 10, 5)
        run_search = st.button("Rechercher dans les notes", type="primary", use_container_width=True)

        st.markdown(
            """
            <div class="warning-box">
                Cette app est une démonstration technique. Elle ne fournit pas de diagnostic médical.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with results_area:
        render_metric_cards(
            [
                ("Dataset", f"{df.shape[0]} lignes"),
                ("Dimensions", "384"),
                ("Source", dataset_source),
            ]
        )

        if dataset_source != "Dataset GitHub Pinecone":
            st.warning(
                "GitHub est inaccessible depuis cette session. "
                "L'app utilise un petit dataset local de secours pour la démo."
            )

        with st.expander("Prévisualiser les données", expanded=False):
            st.dataframe(df.head(10), use_container_width=True)

        if not run_search:
            st.info("Lance une recherche pour interroger l'index Pinecone.")
            return

        with st.spinner("Préparation de l'index Pinecone..."):
            index = ensure_index(pc, index_name, cloud, region)
            stats = index.describe_index_stats()
            vector_count = int(getattr(stats, "total_vector_count", 0))

            if vector_count < len(df):
                upsert_df = prepare_notes_for_upsert(df)
                index.upsert_from_dataframe(upsert_df)
                vector_count = wait_until_fresh(index, expected_count=len(df))

        if vector_count < len(df):
            st.warning(
                "L'index n'a pas encore confirmé toutes les données. "
                "Tu peux relancer la recherche dans quelques secondes."
            )

        with st.spinner("Embedding de la question et recherche vectorielle..."):
            query_vector = get_embedding(question)
            raw_results = index.query(
                vector=query_vector,
                top_k=top_k,
                include_metadata=True,
            )
            matches = [normalize_match(match) for match in raw_results["matches"]]
            matches = sorted(matches, key=lambda match: score_as_float(match.get("score")), reverse=True)

        st.markdown("#### Résultats vectoriels")
        for rank, match in enumerate(matches, start=1):
            metadata = match.get("metadata") or {}
            body = "; ".join(f"{key}: {value}" for key, value in metadata.items())
            render_result_card(rank, score_as_float(match.get("score")), f"ID {match.get('id')}", body)

        transformed_documents = [
            {
                "id": str(match.get("id")),
                "reranking_field": "; ".join(
                    f"{key}: {value}" for key, value in (match.get("metadata") or {}).items()
                ),
            }
            for match in matches
        ]

        with st.spinner("Reranking des résultats..."):
            reranked = pc.inference.rerank(
                model=RERANK_MODEL,
                query=refined_query or question,
                documents=transformed_documents,
                rank_fields=["reranking_field"],
                top_n=min(top_k, len(transformed_documents)),
                return_documents=True,
            )

        st.markdown("#### Résultats rerankés")
        for rank, match in enumerate(reranked.data, start=1):
            document = getattr(match, "document", {}) or {}
            title = f"ID {document.get('id', 'n/a')}"
            render_result_card(
                rank,
                score_as_float(match.score),
                title,
                document.get("reranking_field", ""),
            )


def sidebar_config() -> tuple[str, str, str, str]:
    with st.sidebar:
        st.title("Configuration")
        st.caption("Paramètres Pinecone et index")
        index_name = st.text_input("Nom de l'index", value=DEFAULT_INDEX_NAME)
        cloud = st.text_input("Cloud", value=os.getenv("PINECONE_CLOUD", "aws"))
        region = st.text_input("Région", value=os.getenv("PINECONE_REGION", "us-east-1"))
        st.divider()
        manual_api_key = st.text_input(
            "Cle API Pinecone",
            value="",
            type="password",
            placeholder="pcsk_...",
            help="Optionnel si PINECONE_API_KEY est deja defini dans l'environnement.",
        )
        st.markdown(
            """
            **Clé API**

            Définis `PINECONE_API_KEY` dans ton environnement ou dans `.streamlit/secrets.toml`.
            """
        )
    return (
        index_name.strip() or DEFAULT_INDEX_NAME,
        cloud.strip() or "aws",
        region.strip() or "us-east-1",
        manual_api_key.strip(),
    )


def main() -> None:
    inject_css()
    index_name, cloud, region, manual_api_key = sidebar_config()

    st.markdown(
        """
        <section class="hero">
            <h1>Pinecone Semantic Search</h1>
            <p>
                Une interface Streamlit moderne pour tester le reranking, créer un index serverless
                et rechercher dans des notes médicales avec embeddings.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    api_key = get_pinecone_api_key(manual_api_key)
    if not api_key:
        st.error("Clé Pinecone introuvable. Colle ta clé dans la sidebar ou définis `PINECONE_API_KEY`.")
        st.code(
            "$env:PINECONE_API_KEY = 'ta-cle-api'\nstreamlit run Week7/day2/DailyChallenge/streamlit_app.py",
            language="powershell",
        )
        return

    api_key, api_key_error = validate_pinecone_api_key(api_key)
    if api_key_error:
        st.error(api_key_error)
        st.code("pcsk_...", language="text")
        return

    try:
        pc = get_pinecone_client(api_key)
    except Exception as error:
        st.error(f"Connexion Pinecone impossible : {error}")
        return

    tab_rerank, tab_medical = st.tabs(["Reranking Apple", "Notes médicales"])
    with tab_rerank:
        apple_reranking_tab(pc)
    with tab_medical:
        medical_search_tab(pc, index_name, cloud, region)

    with st.sidebar:
        st.divider()
        if st.button("Supprimer l'index", use_container_width=True):
            try:
                if pc.has_index(name=index_name):
                    pc.delete_index(name=index_name)
                    st.success(f"Index `{index_name}` supprimé.")
                else:
                    st.info("Aucun index à supprimer.")
            except Exception as error:
                st.error(f"Suppression impossible : {error}")


if __name__ == "__main__":
    main()
