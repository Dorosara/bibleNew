import { useState } from 'react';
import { ChakraProvider, Container, VStack, Heading } from '@chakra-ui/react';
import { SearchBox } from './components/SearchBox';
import { SearchResults } from './components/SearchResults';
import { BibleService } from './services/BibleService';
import { verses } from './data/bible';

const bibleService = new BibleService(verses);

function App() {
  const [results, setResults] = useState([]);

  const handleSearch = (query) => {
    const searchResults = bibleService.search(query);
    setResults(searchResults);
  };

  return (
    <ChakraProvider>
      <Container maxW="container.md" py={10}>
        <VStack spacing={8}>
          <Heading>Bible Search App</Heading>
          <SearchBox onSearch={handleSearch} />
          <SearchResults results={results} />
        </VStack>
      </Container>
    </ChakraProvider>
  );
}

export default App;