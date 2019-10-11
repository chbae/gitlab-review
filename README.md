# Python GitLab Review Tool

This tool is for gitlab review.

Author: Changhyeok Bae <changhyeok.bae@gmail.com>

# Requirements

## Install with pip

```
pip install python-gitlab
```

## Setup credentials

In /Users/chanbae/gitlab/gitlab.cfg
```
[swfactory]
url = [GitLab URL]
private_token = [GitLab private token]
api_version = 4
```

# Usage

```
./review.py [Gitlab Merge Request URL]    
```
