---
layout: default
---

# Design a role-playing game using 200 words or less.

This small tabletop game design challenge encourages **everyone** to make a complete role-playing game. It's hard to work on a game, and much harder to finish one. This is an opportunity for participants to brainstorm, write, edit, playtest, and polish a game idea from start to finish.

## 2019 Timeline

- **May.** Begin the search for Judges, Readers, and Prizes. 
- **September.** Contest details posted.
- **October.** The challenge begins!
- **November.** Winners announced, prizes awarded.

## 2019 Judge Suggestions

We are actively searching for a panel of Judges who will help pick this year's winners. **Let us know who you'd like to see on this year's panel!**

 - Tweet your suggestions to [@200WordRPG](https://twitter.com/200WordRPG)
 - Post in the [200 Word Subreddit](https://www.reddit.com/r/200wordrpg)
 - Email our organizers at **200wordrpg (at) gmail (dot) com**.

_Reader applications coming soon (June/July)._

## Why 200 Words?

A 200 word limit encourages creativity and demands the very best of your editing and writing abilities. While making a game in 200 words can be difficult, it’s less of a daunting commitment than editing and proofing 285 pages of rules, complete with art and layout.

Conceiving, designing, and publishing a 200 word game is a great first step toward completing larger game design projects.

## Plaintext?

Visual presentation can be a large and scary problem. Very few people are masters of writing, editing, art direction, graphic design, layout, and marketing. It usually takes a village to make a game. We want participants to focus solely on the challenge of creative writing and brutal editing.

## Licensing and Ownership
Each entry will be publicly posted [on this page]({{site.baseurl}}/2018entries). We reserve the right to reject entries that we consider to be inappropriate or offensive. All entries will be submitted under the Creative Commons Attribution 4.0 International (CC BY 4.0) License. [More info here]({{site.baseurl}}/licensing).

## News & Updates

<p>
{% assign sorted_pages = site.categories.news | sort:"date" | reverse %}
  {% for post in sorted_pages %}
      <h3><strong><a href="{{ post.url }}">
        {{ post.date | date: "%B %d %Y" }} - {{ post.title }}
      </a></strong></h3>
  {% endfor %}
</p>