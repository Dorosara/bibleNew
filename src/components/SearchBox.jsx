import { Input, Button, VStack } from '@chakra-ui/react';

export function SearchBox({ onSearch }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    const query = e.target.search.value;
    onSearch(query);
  };

  return (
    <form onSubmit={handleSubmit}>
      <VStack spacing={4}>
        <Input
          name="search"
          placeholder="Enter your search term"
          size="lg"
        />
        <Button type="submit" colorScheme="blue">
          Search
        </Button>
      </VStack>
    </form>
  );
}