#include "minunit.h"
#include <dlfcn.h>
#include "NAME.h"

char *test_NAME()
{
    return NULL;
}


char *all_tests()
{
    mu_suite_start();

    mu_run_test(test_NAME);

    return NULL;
}

RUN_TESTS(all_tests);
