all: init proto-gen

init:
	@echo "Pull External Protofiles"
	git submodule init
	git submodule update

proto-gen: 
	@echo "Generating Protobuf files"
	./scripts/proto-gen.sh

.PHONY: all proto-gen init
