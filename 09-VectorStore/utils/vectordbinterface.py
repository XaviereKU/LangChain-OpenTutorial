from abc import ABC, abstractmethod
from typing import Any, List, Dict
from langchain_core.documents import Document

class VectorDB(ABC):
    """Abstract class: Interface for interacting with a vector database."""

    @abstractmethod
    def connect(self, **kwargs) -> None:
        """Connects to the DB."""
        pass

    @abstractmethod
    def create_index(self, schema: Dict[str, Any]) -> None:
        """Creates a new index (schema), or return existing index""" # DB에 따라 작업시 해당 인덱스에 연결하여 정보를 불러올 필요가 있는 DB들이 있을 것 같습니다.
        pass

    @abstractmethod
    def delete_index(self, index_or_collection: str) -> None:
        """Deletes a specific index."""
        pass

    @abstractmethod
    def list_indexes(self) -> List[str]:
        """Lists all indexes or collections."""
        pass

    @abstractmethod
    def get_index(self, index_or_collection: str, **kwargs) -> Dict:
        """Get index information."""
        pass

    @abstractmethod
    def insert_documents(self, docs: List[Dict[str, Any]|Document], **kwargs) -> str:
        """Inserts data and a vector."""
        pass

    @abstractmethod
    def update_documents(self, docs: List[Dict[str, Any]|Document], **kwargs) -> bool:
        """Updates existing data."""
        pass

    @abstractmethod
    def replace_documents(self, docs: List[Dict[str, Any]|Document], **kwargs) -> bool:
        """Completely replaces existing data."""
        pass

    @abstractmethod
    def upsert_documents(self, docs: List[Dict[str, Any]|Document], **kwargs) -> str:
        """Inserts or updates data."""
        pass
    
    @abstractmethod
    def upsert_documents_parallel(self, docs: List[Dict[str, Any]|Document], **kwargs) -> str:
        """Inserts or updates data in parallel."""
        pass

    @abstractmethod
    def replace_documents(self, docs: List[Dict[str, Any]|Document], **kwargs) -> bool:
        """Completely replaces existing data."""
        pass

    @abstractmethod
    def update_documents(self, docs: List[Dict[str, Any]|Document], **kwargs) -> bool:
        """Updates existing data."""
        pass

    @abstractmethod
    def delete_documents(self, filter:Any, ids: List[str], query: str, **kwargs) -> bool:
        """Delete data by filter, id or query."""
        pass

    @abstractmethod
    def scroll(self, index_or_collection: str, filter: Any, ids: List[str], query: str, embeddings: bool = False, **kwargs) -> List[Any]:
        """Get data by filter, id, or query."""
        pass

    @abstractmethod
    def similarity_search(self, index_or_collection: str, query: str, top_k: int, score: bool = False, **kwargs) -> List[Any]:
        """Get data based on similarity score."""
        pass

    @abstractmethod
    def as_retriever(self):
        """Returns a Retrieval object."""
        pass
