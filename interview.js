const num_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14];

const div_by_3 = (numbers) => {
  // for (i = 0; i < num_list.length; i++) {
  for (i in numbers) {
    if (numbers[i] % 3 === 0) console.log(numbers[i]);
  }
};

div_by_3(num_list);

k = 4;
k = 'four';
l = k;
