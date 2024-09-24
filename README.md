# otus_test_api

### PART 1
1. https://dog.ceo/dog-api/
    * breeds/list/all
    * breeds/image/random
    * breed/hound/images/random/{num}
    * breed/hound/images/random
    * test_breed_hound_image_random
2. https://jsonplaceholder.typicode.com/
   * todos/
   * all get methods from csv file
   * posts/{num}/comments
3. https://api.openbrewerydb.org/v1/
   * breweries?per_page={per_page}
   * breweries/{_uuid}
   * breweries/random
   * breweries/?{key}={value}&per_page={per_page}

Run tests `pytest -m smoke` or `pytest tests/part1/`

### Part 2
* tests/part2/test_module.py 
* run test `pytest tests/part2/test_module.py --url=https://mail.ru --status_code=200`

