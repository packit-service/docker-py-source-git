.PHONY: check

WORKING_CONT := python-docker-tests-w
TESTS_IMAGE := python-docker-tests
BASE_IMAGE := registry.fedoraproject.org/fedora:29

check:
	ansible-playbook -i inventory-localhost -v -e artifacts=$(CURDIR) -c local ./tests.yml

check-local:
	ansible-playbook -i inventory-localhost -v -e artifacts=$(CURDIR) -c local ./hydrant.yml

build: recipe.yml
	ansible-bender --debug build ./recipe.yml $(BASE_IMAGE) $(TESTS_IMAGE)

check-in-container:
	podman run --rm -ti \
		-v $(CURDIR):/src \
		--net host \
		-e ANSIBLE_PYTHON_INTERPRETER=/usr/bin/python3 \
		-w /src \
		-v /var/run/docker.sock:/var/run/docker.sock \
		$(TESTS_IMAGE) \
		make check-local
