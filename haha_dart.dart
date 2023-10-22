List<int> sequenceGenerator(int start, int stop) {
  return List<int>.generate(stop - start, (index) => start + index);
}

List<dynamic> fizzBuzz(int a, int b) {
  return List<int>.generate(b - a, (index) => a + index)
      .map((num) {
        if (num % 3 == 0 && num % 5 == 0) {
          return "FizzBuzz";
        } else if (num % 3 == 0) {
          return "Fizz";
        } else if (num % 5 == 0) {
          return "Buzz";
        } else {
          return num;
        }
      }).toList();
}


List<int> twoNumbers(List<int> l) {
  List<int> result = [];
  
  void calculateSum(List<int> list) {
    if (list.length < 2) {
      return;
    }
    
    result.add(list[0] + list[1]);
    calculateSum(list.sublist(1));
  }

  calculateSum(l);
  return result;
}


void main() {
  // Output
  print(sequenceGenerator(1, 10));
  print(fizzBuzz(1, 16));
  print(twoNumbers([1, 2, 3, 4, 5]));
}
