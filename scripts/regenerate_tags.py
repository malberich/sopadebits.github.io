#!/usr/bin/python

import os
import glob
import yaml
import frontmatter
import re
from slugify import slugify

if __name__ == '__main__':

    tags = dict()
    categories = dict()

    title_re = re.compile(r'^(\d+)-(\d+)-(\d+)-(.*)\.(md|html)$')

    post_list = glob.glob(os.path.expanduser("./_posts/*"))
    post_list.sort(reverse=True)

    if not os.path.isdir(os.path.expanduser("./_data")):
        os.mkdir(os.path.expanduser("./_data"))

    if not os.path.isdir(os.path.expanduser("./_tag")):
        os.mkdir(os.path.expanduser("./_tag"))

    if not os.path.isdir(os.path.expanduser("./_category")):
        os.mkdir(os.path.expanduser("./_category"))



    for file in post_list:
        filename = os.path.basename(
            os.path.realpath(file)
        )

        print(filename)
        title_parts = title_re.findall(filename)
        print(title_parts)
        post_slug = title_parts[0][3]
        print(post_slug)
        post = frontmatter.Frontmatter.read_file(os.path.expanduser(file))
        # post_slug = slugify(
        #     post['attributes']['title'].lower(),
        #     separator='-',
        #     replacements=[
        #         ['á', 'a'],
        #         ['é', 'e'],
        #         ['í', 'i'],
        #         ['ó', 'o'],
        #         ['ú', 'u'],
        #         ['ñ', 'n'],
        #         ['ç', 's']
        #     ]
        # )
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

            tags[slug_tag]['posts'].append({
                'filename': filename,
                'title': post['attributes']['title'],
                'url': post_slug,
                'date': post['attributes']['date']
            })

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

            categories[slug_cat]['posts'].append({
                'filename': filename,
                'title': post['attributes']['title'],
                'url': post_slug,
                'date': post['attributes']['date']
            })

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
        with open(os.path.expanduser("./_tag/{}.md".format(tag_slug)), "w+") as f:
            f.write(
                "---\nlayout: tagpage\ngroup_type: tag\ntitle: \"Tag: {tagname}\"\ntag: {tag_slug}\n---".format(
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
        with open(os.path.expanduser("./_category/{}.md".format(slug_cat)), "w+") as f:
            f.write(
                "---\nlayout: tagpage\ngroup_type: category\ntitle: \"Category: {catname}\"\ntag: {slug_cat}\n---".format(
                    catname=cat['name'],
                    slug_cat=slug_cat
                )
            )
            f.close()
