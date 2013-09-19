describe('binary search tests', function() {

  beforeEach(function() {
  });

  afterEach(function() {
  });

  it('should test binaryChop', function() {
    expect(BinarySearch.binaryChop(3, [])).toEqual(-1);
    expect(BinarySearch.binaryChop(3, [1])).toEqual(-1);
    expect(BinarySearch.binaryChop(1, [1])).toEqual(0);
    expect(BinarySearch.binaryChop(1, [1, 3, 5])).toEqual(0);
    expect(BinarySearch.binaryChop(3, [1, 3, 5])).toEqual(1);
    expect(BinarySearch.binaryChop(5, [1, 3, 5])).toEqual(2);
    expect(BinarySearch.binaryChop(0, [1, 3, 5])).toEqual(-1);
    expect(BinarySearch.binaryChop(2, [1, 3, 5])).toEqual(-1);
    expect(BinarySearch.binaryChop(4, [1, 3, 5])).toEqual(-1);
    expect(BinarySearch.binaryChop(6, [1, 3, 5])).toEqual(-1);
    expect(BinarySearch.binaryChop(1, [1, 3, 5, 7])).toEqual(0);
    expect(BinarySearch.binaryChop(3, [1, 3, 5, 7])).toEqual(1);
    expect(BinarySearch.binaryChop(5, [1, 3, 5, 7])).toEqual(2);
    expect(BinarySearch.binaryChop(7, [1, 3, 5, 7])).toEqual(3);
    expect(BinarySearch.binaryChop(0, [1, 3, 5, 7])).toEqual(-1);
    expect(BinarySearch.binaryChop(2, [1, 3, 5, 7])).toEqual(-1);
    expect(BinarySearch.binaryChop(4, [1, 3, 5, 7])).toEqual(-1);
    expect(BinarySearch.binaryChop(6, [1, 3, 5, 7])).toEqual(-1);
    expect(BinarySearch.binaryChop(8, [1, 3, 5, 7])).toEqual(-1);
  });

});
