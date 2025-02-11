from enum import Enum


class PromptServiceContants:
    WORD = "word"
    SYNONYMS = "synonyms"
    OUTPUTS = "outputs"
    TOOL_ID = "tool_id"
    FILE_NAME = "file_name"
    FILE_HASH = "file_hash"
    NAME = "name"
    ACTIVE = "active"
    PROMPT = "prompt"
    CHUNK_SIZE = "chunk-size"
    PROMPTX = "promptx"
    VECTOR_DB = "vector-db"
    EMBEDDING = "embedding"
    X2TEXT_ADAPTER = "x2text_adapter"
    CHUNK_OVERLAP = "chunk-overlap"
    LLM = "llm"
    IS_ASSERT = "is_assert"
    ASSERTION_FAILURE_PROMPT = "assertion_failure_prompt"
    RETRIEVAL_STRATEGY = "retrieval-strategy"
    SIMPLE = "simple"
    TYPE = "type"
    NUMBER = "number"
    EMAIL = "email"
    DATE = "date"
    BOOLEAN = "boolean"
    JSON = "json"
    PREAMBLE = "preamble"
    SIMILARITY_TOP_K = "similarity-top-k"
    PROMPT_TOKENS = "prompt_tokens"
    COMPLETION_TOKENS = "completion_tokens"
    TOTAL_TOKENS = "total_tokens"
    RESPONSE = "response"
    POSTAMBLE = "postamble"
    GRAMMAR = "grammar"
    PLATFORM_SERVICE_API_KEY = "PLATFORM_SERVICE_API_KEY"
    EMBEDDING_SUFFIX = "embedding_suffix"
    EVAL_SETTINGS = "eval_settings"
    EVAL_SETTINGS_EVALUATE = "evaluate"
    EVAL_SETTINGS_MONITOR_LLM = "monitor_llm"
    EVAL_SETTINGS_EXCLUDE_FAILED = "exclude_failed"
    TOOL_SETTINGS = "tool_settings"
    LOG_EVENTS_ID = "log_events_id"
    CHALLENGE_LLM = "challenge_llm"


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class RunLevel(Enum):
    """Different stages of prompt execution.

    Comprises of prompt run and response evaluation stages.
    """

    RUN = "RUN"
    EVAL = "EVAL"
    CHALLENGE = "CHALLENGE"
