import { Box, Text, VStack } from '@chakra-ui/react';

export function SearchResults({ results }) {
  if (!results.length) {
    return <Text>No results found</Text>;
  }

  return (
    <VStack spacing={4} align="stretch">
      {results.map((result, index) => (
        <Box key={index} p={4} borderWidth={1} borderRadius="md">
          <Text>{result}</Text>
        </Box>
      ))}
    </VStack>
  );
}