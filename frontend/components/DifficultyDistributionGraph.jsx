import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const DifficultyDistributionGraph = ({ difficultyDistribution }) => {
  const maxDifficulty = Math.max(...difficultyDistribution);

  return (
    <View style={styles.container}>
      {difficultyDistribution.map((difficulty, index) => (
        <View key={index} style={styles.barContainer}>
          <View style={[styles.bar, { height: (difficulty / maxDifficulty) * 100 }]} />
          <Text style={styles.barText}> {difficulty}%</Text>
          <Text style={styles.barText}> {index + 1}</Text>
        </View>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    justifyContent: 'space-evenly',
    alignItems: 'flex-end',
    paddingHorizontal: 10,
    height: 150,
  },
  barContainer: {
    flex: 1,
    alignItems: 'center',
  },
  bar: {
    width: 20,
    backgroundColor: 'lightblue',
    borderRadius: 5,
    marginHorizontal: 2,
  },
  barText: {
    textAlign: 'center',
    color: 'white',
    fontWeight: 'bold',
    fontSize: 12,
    marginTop: 5,
  },
});

export default DifficultyDistributionGraph;
