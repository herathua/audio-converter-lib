#include <node_api.h>

// Function that adds two numbers
napi_value Add(napi_env env, napi_callback_info args) {
    size_t argc = 2;
    napi_value argv[2];

    // Parse the arguments
    napi_get_cb_info(env, args, &argc, argv, NULL, NULL);

    double num1, num2;
    napi_get_value_double(env, argv[0], &num1);
    napi_get_value_double(env, argv[1], &num2);

    napi_value result;
    napi_create_double(env, num1 + num2, &result);
    return result;
}

// Initialization function for the module
napi_value Init(napi_env env, napi_value exports) {
    napi_value add_function;
    napi_create_function(env, NULL, 0, Add, NULL, &add_function);
    napi_set_named_property(env, exports, "add", add_function);
    return exports;
}

// Module entry point
NAPI_MODULE(NODE_GYP_MODULE_NAME, Init)
