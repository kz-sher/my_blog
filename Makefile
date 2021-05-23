prebuild:
	python3 scripts/tag_generator.py
	python3 scripts/md_heading_with_link_substitutor.py

build: prebuild
	bundle exec jekyll build

serve: prebuild
	bundle exec jekyll serve