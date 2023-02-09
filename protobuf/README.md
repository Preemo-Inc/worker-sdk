# protobuf

This subrepo contains all the proto files for the Preemo Worker SDK.

## Getting Started

The documentation for protocol buffers can be found here: https://protobuf.dev/overview/.

## Updating Proto Files

The protobuf protocol was designed to be backwards (and forwards) compatible. However, in order to maintain compatibility, there are several rules and conventions that must be followed when making updates.

A list of best practices can be found here: https://protobuf.dev/programming-guides/dos-donts/. Some of the most important rules are summarized below.

### Creating a Field

When creating a field, ensure that the name and tag of the new field has never been used in that message.

#### Field Types

Be thoughtful about the type you choose. Most types cannot be changed into any other types without breaking compatibility. All scalar types can be found here: https://protobuf.dev/programming-guides/proto3/#scalar

#### Field Rules

While proto3 syntax allows `singular` as a field rule, our convention is to always use `optional` instead. The main difference is that `optional` allows you to determine if the field was explicitly set, while `singular` does not.

### Deleting a Field

When deleting a field from a protobuf message, use the `reserved` keyword to reserve the field's name and tag to ensure it is not accidentally re-used. In addition, comment out the field with an explanation of why it has been removed.

For example, if you start with the following `Example` message:
```
message Example {
  optional string foo = 1;
  optional string bar = 2;
  optional string baz = 3;
}
```

In order to delete `bar`, you could update it as follows:
```
message Example {
  optional string foo = 1;

  // DEPRECATED optional string bar = 2;
  reserved "bar";
  reserved 2;

  optional string baz = 3;
}
```

### Creating an Enum

Enum values use C++ scoping rules, meaning that enum values are siblings of their type, not children of it. So enum values should be prefixed with the name of the enum to keep them unique within the global scope. Additionally, enums must always have an "unspecified" value with the tag 0. This unspecified value will serve as the default value for the enum.

For example:
```
enum Example {
  EXAMPLE_UNSPECIFIED = 0;
  EXAMPLE_VALUE_A = 1;
  EXAMPLE_VALUE_B = 2;
  ...
}
```
