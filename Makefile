prebuild:
	python3 scripts/tag_generator.py
	python3 scripts/linked_md_heading_substitutor.py

build: prebuild
	bundle exec jekyll build

serve: prebuild
	bundle exec jekyll serve