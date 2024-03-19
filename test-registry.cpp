#include <test-registry.h>

#include <fmt/format.h>

#include <chrono>
#include <iostream>
#include <ostream>
#include <ratio>
#include <string>
#include <utility>

auto TestRegistry::instance() noexcept -> TestRegistry& {
  static auto testRegistry = TestRegistry{};
  return testRegistry;
}

auto TestRegistry::addTest(TestParameters test) noexcept -> TestIndexT {
  m_testList.emplace_back(std::move(test));
  return m_testList.size();
}

auto TestRegistry::executeTests() const noexcept -> void {
  auto testCounter  = 0U;
  auto testResult   = std::string{};
  auto testDuration = std::chrono::microseconds{};

  for (const auto& [testName, testEntry] : m_testList) {
    const auto start = std::chrono::steady_clock::now();
    const auto ok    = testEntry();
    const auto end   = std::chrono::steady_clock::now();

    testCounter  = (testCounter + 1);
    testResult   = ok ? std::string{"OK"} : std::string{"NG"};
    testDuration = std::chrono::duration_cast<decltype(testDuration)>(end - start);

    const auto testDurationMs = (testDuration.count() / std::milli::den);
    const auto testDurationUs = (testDuration.count() % std::milli::den);

    const auto message = fmt::format("{:03}) {} [{}] - {}.{} (ms)",
      testCounter,
      testName,
      testResult,
      testDurationMs,
      testDurationUs);

    std::cout << message << '\n';
    std::flush(std::cout);
  }
}
