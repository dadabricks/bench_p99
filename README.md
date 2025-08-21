# bench-p99

This is a benchmark repository generated for testing purposes.

## Repository Statistics

### Target Specifications
- **Repository Name**: bench-p99
- **Remote URL**: https://github.com/dadabricks/bench_p99.git
- **Notebook Count**: 4000
- **Dashboard Count**: 99
- **Text File Count**: 4000
- **Query Count**: 99
- **Folder Count**: 4000
- **Target Worktree Size**: 243,794,929 bytes
- **Target .git Folder Size**: 169,398,930 bytes

### Actual Results
- **Final Worktree Size**: 243,794,929 bytes
- **Final .git Folder Size**: 240,055,357 bytes
- **Total Repository Size**: 483,850,286 bytes

### Directory Structure
```
bench-p99/
├── README.md                 # This file
├── assets/                   # All generated assets
│   ├── notebook_*.ipynb      # 4000 notebook files
│   ├── dashboard_*.lvdash.json # 99 dashboard files
│   ├── text_*.md            # 4000 text files
│   └── query_*.dbalert.json # 99 query files
├── folders/                  # Generated folder structure
│   └── folder_*/             # 4000 folders with subfolders
└── padding/                  # Padding files to reach target worktree size
    └── padding_data_*.bin    # Multiple files, each <50MB for GitHub compatibility
```

## Generation Information
- **Generated on**: 2025-08-21 13:33:44
- **Tool**: build_bench_repos.py
- **Purpose**: Benchmark repository for testing git metrics and repository analysis tools

## Notes
- All assets are copies of template files from the static_assets directory
- The .git folder has been artificially inflated using commit bloat techniques
- The worktree has been padded with random data to reach the target size
- File names include UUID suffixes for uniqueness
