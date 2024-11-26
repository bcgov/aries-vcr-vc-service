from typing import Annotated, List
from fastapi import Body
from pydantic import BaseModel
from schemas import Signed


class SignedCredential(Signed, BaseModel):
    """SignedCredential schema"""

    context: Annotated[
        list[str], Body(validation_alias="@context", serialization_alias="@context")
    ]
    id: str
    type: List[str] | str
    issuer: str | dict
    validFrom: str
    validUntil: str = None
    name: str | dict | None = None
    description: str | dict | None = None
    credentialSubject: dict
    credentialSchema: List[dict] | dict = None
    credentialStatus: List[dict] | dict = None
    refreshService: List[dict] | dict = None
    renderMethod: List[dict] | dict = None
    termsOfUse: List[dict] | dict = None
    relatedResources: List[dict] | dict = None
    proof: List[dict] | dict = None
