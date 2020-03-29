#!/usr/bin/python

import os
import glob
import yaml
import frontmatter
from slugify import slugify

if __name__ == '__main__':

    tags = dict()
    categories = dict()

    post_list = glob.glob(os.path.expanduser("./_posts/*"))
    post_list.sort(reverse=True)

    if not os.path.isdir(os.path.expanduser("./_data")):
        os.mkdir(os.path.expanduser("./_data"))

    if not os.path.isdir(os.path.expanduser("./tag")):
        os.mkdir(os.path.expanduser("./tag"))

    if not os.path.isdir(os.path.expanduser("./category")):
        os.mkdir(os.path.expanduser("./category"))

    for file in post_list:
        print(file)
        filename = os.path.basename(
            os.path.realpath(file)
        )
        post = frontmatter.Frontmatter.read_file(os.path.expanduser(file))
        print(list(post.keys()))
        for tag in post['attributes']['tags']:
            slug_tag = slugify(
                tag.lower(),
                separator='-',
                replacements=[
                    ['á', 'a'],
                    ['é', 'e'],
                    ['í', 'i'],
                    ['ó', 'o'],
                    ['ú', 'u'],
                    ['ñ', 'n'],
                    ['ç', 's']
                ]
            )
            if slug_tag not in tags.keys():
                tags[slug_tag] = dict()
                tags[slug_tag]['name'] = tag
                tags[slug_tag]['slug'] = slug_tag
                tags[slug_tag]['posts'] = list()

            tags[slug_tag]['posts'].append(filename)

        for category in post['attributes']['categories']:
            slug_cat = slugify(
                category.lower(),
                separator='-',
                replacements=[
                    ['á', 'a'],
                    ['é', 'e'],
                    ['í', 'i'],
                    ['ó', 'o'],
                    ['ú', 'u'],
                    ['ñ', 'n'],
                    ['ç', 's']
                ]
            )
            if slug_cat not in categories.keys():
                categories[slug_cat] = dict()
                categories[slug_cat]['name'] = category
                categories[slug_cat]['slug'] = slug_cat
                categories[slug_cat]['posts'] = list()

            categories[slug_cat]['posts'].append(filename)

    with open(os.path.expanduser("./_data/tags.yml"), "w+") as f_tags:
        yaml.dump(tags, f_tags)

    with open(os.path.expanduser("./_data/categories.yml"), "w+") as f_cats:
        yaml.dump(categories, f_cats)

    for file in glob.glob(
        os.path.expanduser(
            "./_tag/*"
        )
    ):
        os.remove(file)

    for (tag_slug, tag) in tags.items():
        with open(os.path.expanduser("./tag/{}.md".format(tag_slug)), "w+") as f:
            f.write(
                "---\nlayout: tagpage\ntitle: \"Tag: {tagname}\"\ntag: {tag_slug}\n---".format(
                    tagname=tag['name'],
                    tag_slug=tag_slug
                )
            )
            f.close()

    for file in glob.glob(
        os.path.expanduser(
            "./_category/*"
        )
    ):
        os.remove(file)

    for (slug_cat, cat) in categories.items():
        with open(os.path.expanduser("./category/{}.md".format(slug_cat)), "w+") as f:
            f.write(
                "---\nlayout: tagpage\ntitle: \"Category: {catname}\"\ntag: {slug_cat}\n---".format(
                    catname=cat['name'],
                    slug_cat=slug_cat
                )
            )
            f.close()
