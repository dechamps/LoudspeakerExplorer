{ gsub( \
    /###INJECT_LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA###/, \
    "LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA = '" ENVIRON["GITHUB_SHA"] "'") }

{
    build_time = strftime()
    if (ENVIRON["GITHUB_RUN_ID"])
        build_time = "[" build_time "](https://github.com/" ENVIRON["GITHUB_REPOSITORY"] "/actions/runs/" ENVIRON["GITHUB_RUN_ID"] ")"
    gsub(/<!--BUILDINFO-->/, \
        " - _[Changelog](https://github.com/" ENVIRON["GITHUB_REPOSITORY"] "/commits/" ENVIRON["GITHUB_SHA"] \
        ") (built from [" substr(ENVIRON["GITHUB_SHA"], 0, 7) "](https://github.com/" ENVIRON["GITHUB_REPOSITORY"] "/commit/" ENVIRON["GITHUB_SHA"] \
        ") on " build_time ")_")
}

1