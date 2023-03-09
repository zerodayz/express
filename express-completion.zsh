_express_run (){
  _arguments \
    '--number[Number of cores to run on]' \
    '-n[Number of cores to run on]' \
    '--headless[Run tests in headless mode]' \
    '-H[Run tests in headless mode]' \
    '--list[List all tests]' \
    '-l[List all tests]' \
    '*--browser[Specify a browser to run the tests]:browser name:(firefox chrome)' \
    '*-b[Specify a browser to run the tests]:browser name:(firefox chrome)' \
    '--ignore[Ignore a test]' \
    '-i[Ignore a test]' \
    '-h[Show help]' \
    '--help[Show help]' \
    '*:test file:_files -g "test_*.py"'
}

compdef _express_run express-run