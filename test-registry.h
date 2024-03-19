#pragma once

#include <functional>
#include <string>
#include <vector>

class TestRegistry final {
public:

  static TestRegistry& instance() noexcept;

  struct TestParameters {
    std::string name{};
    std::function<bool()> entry{};
  };

  using TestIndexT = std::size_t;
  TestIndexT addTest(TestParameters test) noexcept;
  void executeTests() const noexcept;

private:

  std::vector<TestParameters> m_testList{};
};

#define REGISTER_TEST(name, entry) \
  static const auto INDEX_##entry = TestRegistry::instance().addTest({name, entry});
