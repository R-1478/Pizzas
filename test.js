function solution(N) {
    string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if (N <= string.length){
      response = (string.slice(0, N)).toString()
      console.log(response)
      return response
      
    }
    else if (N > string.length);
     let n = []
     while (n.length < N) {
      for (const str of string){
          newstr = str.repeat(2)
          new1 = newstr.slice(0)
          new2 = newstr.slice(1)
          

          n.push(new2, new2)
      }
     }
     console.log((n.slice(0, N)).toString())}

  solution(100)

  // Task description
  // Write a function solution that, given an integer N, returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.
  
  // Examples:
  // while (N > string.length);
  // response = ((str).toString()) * 2;
  // console.log(response); 
  
  // Given N = 3, the function may return "fig", "pea", "nut", etc. Each of these strings contains three different letters with the same number of occurrences.
  // Given N = 5, the function may return "mango", "grape", "melon", etc.
  // Given N = 30, the function may return "aabbcc...oo" (each letter from 'a' to 'o' occurs twice). The string contains 15 different letters.
  // Write an efficient algorithm for the following assumptions:
  
  // N is an integer within the range [1..200,000].