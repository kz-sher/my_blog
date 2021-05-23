build:
	python3 scripts/tag_generator.py
	bundle exec jekyll build

serve:
	python3 scripts/tag_generator.py
	bundle exec jekyll serve