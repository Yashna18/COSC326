/*
 *The following file is the header file for
 * the Integer class defined in Integer.cpp
 * @author Yashna Shetty
 * @author Cameron Moore-Carter
 */
#pragma once
// Most compilers understand the once pragma, but just in case...
#ifndef INTEGER_H_INCLUDED
#define INTEGER_H_INCLUDED

#include <iostream>
#include <string>
#include <vector>

namespace cosc326 {
	
	class Integer {
	
	public:
		
		// Structure
		bool sign;
		int capacity;
		int numDigits;
		char *digits;
		Integer();                             // Integer i;
		Integer(const Integer& i);             // Integer j(i);
		Integer(const std::string& s);         // Integer k("123");
		Integer(const int& i);
		~Integer();

		// Helper Functions 
		friend Integer longDivision(Integer& lhs, int i);
		friend int toInt(Integer& i);
		Integer& operator=(const Integer& i);  // j = i;
		friend Integer operator/(const Integer& lhs, const Integer& rhs); // lhs / rhs;

		// Unary operators
		Integer operator-() const;                   // -j;
		Integer operator+() const;                   // +j;

		// Arithmetic assignment operators
		Integer& operator+=(const Integer& i); // j += i;
		Integer& operator-=(const Integer& i); // j -= i;
		Integer& operator*=(const Integer& i); // j *= i;
		Integer& operator/=(const Integer& i); // j /= i;
		Integer& operator%=(const Integer& i); // j %= i;
		
		// lhs < rhs -- a 'friend' means operator isn't a member, but can access the private parts of the class.
		// You may need to make some other functions friends, but do so sparingly.
		friend bool operator<(const Integer& lhs, const Integer& rhs);

	private:
		std::vector<int> data;
		// Can add internal storage or methods here
		#define MAX(i1, i2) (i1 > i2 ? i1 : i2)
		
		
	};

	// Binary operators
	Integer operator+(const Integer& lhs, const Integer& rhs); // lhs + rhs;
	Integer operator-(const Integer& lhs, const Integer& rhs); // lhs - rhs;
	Integer operator*(const Integer& lhs, const Integer& rhs); // lhs * rhs;
	
	Integer operator%(const Integer& lhs, const Integer& rhs); // lhs % rhs;

	std::ostream& operator<<(std::ostream& os, const Integer& i);  // std::cout << i << std::endl;
	std::istream& operator>>(std::istream& is, Integer& i);        // std::cin >> i;
	
	bool operator> (const Integer& lhs, const Integer& rhs); // lhs > rhs
	bool operator<=(const Integer& lhs, const Integer& rhs); // lhs <= rhs
	bool operator>=(const Integer& lhs, const Integer& rhs); // lhs >= rhs
	bool operator==(const Integer& lhs, const Integer& rhs); // lhs == rhs
	bool operator!=(const Integer& lhs, const Integer& rhs); // lhs != rhs

	Integer gcd(const Integer& a, const Integer& b);  // i = gcd(a, b);
	extern const Integer INTEGER_ZERO;
	
	
}

#endif
