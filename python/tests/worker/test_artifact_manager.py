from preemo.worker._artifact_manager import (
    ArtifactManager,
    IArtifactManager,
    LocalArtifactManager,
)


class TestArtifactManager:
    def test_fulfills_protocol(self) -> None:
        assert isinstance(ArtifactManager, IArtifactManager)


class TestLocalArtifactManager:
    def test_fulfills_protocol(self) -> None:
        assert isinstance(LocalArtifactManager, IArtifactManager)
