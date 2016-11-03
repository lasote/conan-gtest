// Thanks to http://joeyates.info/2010/05/26/googletest-hello-world/ for the example!

/////////////////////////////
// In the header file

#include <sstream>
using namespace std;

class Salutation
{
public:
  static string greet(const string& name);
};

///////////////////////////////////////
// In the class implementation file

string Salutation::greet(const string& name) {
  ostringstream s;
  s << "Hello " << name << "!";
  return s.str();
}

///////////////////////////////////////////
// In the test file
#include <gtest/gtest.h>

TEST(SalutationTest, Static) {
  EXPECT_EQ(string("Hello World!"), Salutation::greet("World"));
}
