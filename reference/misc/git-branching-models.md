---
doc_id: "mta-wiki:9065"
title: "Git Branching Models"
source_title: "Git Branching Models"
source_url: "https://wiki.multitheftauto.com/wiki/Git_Branching_Models"
revision_id: 49031
language: "en"
categories: []
generated_at: "2026-07-26T16:15:30.930347+00:00"
---

# Git Branching Models

Our current branching model is not optimal and makes keeping track of versions hard.
This page discusses various branching models.

## Models

### Current SVN-like Model

- *master* is the development branch which contains incompatible code as well

- A version branch e.g. *1.5.2* is created when releasing a new stable version

- 'Stable commits' are merged from *master* frequently (==> rolling release like)

- We'd need something like [http://i.imgur.com/sAWIOel.png](http://i.imgur.com/sAWIOel.png)

##### Pros

- Easy management of incompatible code (==> rolling-release works well)

##### Cons

- Prone to losing track of differences between master and version branches

- Doesn't integrate well with popular Git models implemented on e.g. GitHub

### Feature Branches

- New, maybe incompatible features are implemented in separate branches and merged as soon as they are stable

- *master* is mostly stable

- When releasing a new version, a tag is created from master

- Release intervals are smaller

#### Feature Branches Example

- Current version is 1.5

- Someone wants to implement complicated things which are netcode-incompatible with 1.5

- Someone creates feature/complicated-things branched from master

- Work is now done on feature/complicated-things

- Once feature/complicated-things is ready it needs to wait for 1.6

- (time passes)

- (1.6 is ready for release)

- master is tagged as 1.5.x-final marking the end of 1.5 compatibility

- master version number is increased to 1.6

- feature/complicated-things is merged into master

- master build gets released to the public

#### Pros

- "Git"-way (==> integrates well with GitHub)

- No weird cherry-picking is necessary

#### Cons

- We have to modify our nightly system and build server settings to support feature branches somehow (required for properly distributing tests)

- We could probably use Travis CI and AppVeyor to easily maintain public builds for feature branches [Sbx320](https://wiki.multitheftauto.com/index.php?title=User:Sbx320&action=edit&redlink=1) ([talk](https://wiki.multitheftauto.com/index.php?title=User_talk:Sbx320&action=edit&redlink=1)) 18:33, 9 August 2016 (UTC)

## Comments

- My concerns over Feature Branches are largely based upon any added bureaucracy or complexity to making contributions.  --[Talidan](https://wiki.multitheftauto.com/wiki/User:Talidan) ([talk](https://wiki.multitheftauto.com/wiki/User_talk:Talidan)) 18:04, 9 August 2016 (UTC)

- I don't think so: I'd rather think it removes bureucracy as we don't have to cherry-pick commits to 1.5.x any longer and lose track of merged/unmerged commits --[Jusonex](https://wiki.multitheftauto.com/wiki/User:Jusonex) ([talk](https://wiki.multitheftauto.com/index.php?title=User_talk:Jusonex&action=edit&redlink=1)) 16:55, 5 September 2016 (UTC+2)
