# protoc does not and will not generate relative imports for python.
# This workaround was copied from https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-429735834:
import os
import sys

sys.path.append(os.path.dirname(__file__))