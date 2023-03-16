from preemo.worker._artifact_manager import ArtifactManager, IArtifactManager


class TestArtifactManager:
    def test_fulfills_protocol(self) -> None:
        assert isinstance(ArtifactManager, IArtifactManager)
