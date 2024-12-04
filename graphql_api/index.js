const { ApolloServer, gql } = require('apollo-server');

// Sample data
const items = [
  { id: 1, name: "Item 1" },
  { id: 2, name: "Item 2" }
];

// GraphQL schema
const typeDefs = gql`
  type Item {
    id: Int
    name: String
  }

  type Query {
    items: [Item]
    item(id: Int!): Item
  }

  type Mutation {
    addItem(name: String!): Item
    deleteItem(id: Int!): String
  }
`;

// Resolvers
const resolvers = {
  Query: {
    items: () => items,
    item: (_, { id }) => items.find(item => item.id === id)
  },
  Mutation: {
    addItem: (_, { name }) => {
      const newItem = { id: items.length + 1, name };
      items.push(newItem);
      return newItem;
    },
    deleteItem: (_, { id }) => {
      const index = items.findIndex(item => item.id === id);
      if (index === -1) return "Item not found";
      items.splice(index, 1);
      return "Item deleted";
    }
  }
};

// Apollo Server setup
const server = new ApolloServer({ typeDefs, resolvers });

// Start server
server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
