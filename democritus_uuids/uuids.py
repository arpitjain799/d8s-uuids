import uuid
from typing import List, Union, Optional


def uuid4_examples(n: int = 10, *, uuids_as_strings: bool = True) -> Union[List[str], List[uuid.UUID]]:
    """Create n uuids."""
    from hypothesis.strategies import uuids

    from democritus_hypothesis import hypothesis_get_strategy_results

    uuid_objects = hypothesis_get_strategy_results(uuids, n=n)
    if uuids_as_strings:
        return [str(uuid) for uuid in uuid_objects]
    else:
        return uuid_objects


def uuid4() -> str:
    """Create a random UUID."""
    return str(uuid.uuid4())


def uuid3(name: str, *, namespace: Optional[uuid.UUID] = None) -> str:
    """Create a random uuid based on the given name."""
    if namespace is None:
        namespace = uuid.NAMESPACE_DNS

    return str(uuid.uuid3(namespace, name))


def uuid5(name: str, *, namespace: Optional[uuid.UUID] = None) -> str:
    """Create a random uuid based on the given name."""
    if namespace is None:
        namespace = uuid.NAMESPACE_DNS

    return str(uuid.uuid5(namespace, name))


def is_uuid(possible_uuid: Union[str, uuid.UUID], *, version: Optional[int] = None) -> bool:
    """Return whether or not the possible_uuid is a uuid."""
    try:
        new_uuid = uuid.UUID(possible_uuid)
    except ValueError as e:
        return False
    else:
        if version is not None:
            if new_uuid.version != version:
                return False
        return True
