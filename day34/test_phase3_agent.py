import os
import sys

import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DAY30_PATH = os.path.join(PROJECT_ROOT, "day30")
sys.path.insert(0, DAY30_PATH)

import phase3_agent as agent_module


@pytest.fixture
def agent():
    return agent_module.Phase3Agent(agent_module.DOCUMENTS)


def test_tokenize_and_normalize_handles_basic_text():
    assert agent_module.tokenize("Passwords must be changed every 90 days!") == [
        "passwords",
        "must",
        "be",
        "changed",
        "every",
        "90",
        "days",
    ]
    assert agent_module.normalize_token("days") == "day"
    assert agent_module.normalize_token("policies") == "policy"


def test_content_tokens_removes_stopwords_and_normalizes():
    assert agent_module.content_tokens("What is our password policy?") == ["password", "policy"]


def test_vectorize_counts_normalized_tokens():
    assert agent_module.vectorize("Passwords and passwords") == {"password": 2}


def test_cosine_similarity_handles_empty_vectors():
    assert agent_module.cosine_similarity({}, {}) == 0.0


def test_route_direct_for_small_talk(agent):
    route, reason = agent.route("Hello there")

    assert route == "direct"
    assert reason == "general question"


def test_route_retrieve_for_policy_question(agent):
    route, reason = agent.route("What is the password policy?")

    assert route == "retrieve"
    assert "password" in reason


def test_route_declines_for_unsupported_question(agent):
    route, reason = agent.route("Tell me about PTO")

    assert route == "decline"
    assert reason == "no document topic match"


def test_retrieve_returns_best_matching_chunk(agent):
    chunks, top_matches = agent.retrieve("What is the password policy?")

    assert chunks[0] == "Passwords must be changed every 90 days."
    assert top_matches[0][0] == 3
    assert top_matches[0][1] > top_matches[1][1]


def test_answer_direct_returns_help_message(agent):
    assert agent.answer_direct("Hello") == (
        "Hello. I can answer questions about the sample policy documents."
    )


def test_answer_grounded_returns_policy_answer(agent):
    result = agent.answer_grounded("What is the password policy?")

    assert result["mode"] == "retrieve"
    assert "Passwords must be changed every 90 days." in result["answer"]
    assert result["retrieved_chunks"][0] == "Passwords must be changed every 90 days."


def test_answer_grounded_declines_when_confidence_is_low(agent):
    result = agent.answer_grounded("What is our PTO policy?")

    assert result["mode"] == "decline"
    assert result["answer"] == "I don't know based on the provided documents."


def test_run_direct_branch(agent, capsys):
    result = agent.run("What can you do?")
    captured = capsys.readouterr()

    assert result["route"] == "direct"
    assert result["answer"].startswith("I can decide whether to retrieve")
    assert "Router decision: direct" in captured.out


def test_run_retrieve_branch(agent, capsys):
    result = agent.run("What is the password policy?")
    captured = capsys.readouterr()

    assert result["route"] == "retrieve"
    assert result["retrieved_chunks"][0] == "Passwords must be changed every 90 days."
    assert "Router decision: retrieve" in captured.out


def test_run_decline_branch(agent, capsys):
    result = agent.run("Tell me about PTO")
    captured = capsys.readouterr()

    assert result["route"] == "decline"
    assert result["answer"] == "I don't know based on the provided documents."
    assert "Router decision: decline" in captured.out
