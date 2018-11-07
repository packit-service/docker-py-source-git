.PHONY: check

WORKING_CONT := python-docker-tests-w
TESTS_IMAGE := python-docker-tests
BASE_IMAGE := registry.fedoraproject.org/fedora:29

check:
	ansible-playbook -i inventory-localhost -v -e artifacts=$(CURDIR) -c local ./tests.yml

build:
	sudo podman run \
		--name $(WORKING_CONT) \
		$(BASE_IMAGE) \
		dnf install -y standard-test-roles make
	sudo podman commit $(WORKING_CONT) $(TESTS_IMAGE)
	sudo podman rm $(WORKING_CONT)

check-in-container:
	sudo podman run --rm \
		-v $(CURDIR):/src \
		--net host \
		-w /src \
		-v /var/run/docker.sock:/var/run/docker.sock \
		$(TESTS_IMAGE) \
		make check
