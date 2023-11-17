import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import DifficultyDistributionGraph from './DifficultyDistributionGraph';

const LevelDetails = ({ level,levelData, lastest, onStart, onClose }) => {
    console.log(levelData)
  return (
    <LinearGradient colors={['rgba(0, 0, 50, 0.9)', 'rgba(0, 0, 50, 0.7)']} style={styles.gradient}>
      <View style={styles.container}>
        <View style={styles.modal}>
          <Text style={styles.title}>{`Level ${level.level_index} ${levelData.level_name}`}</Text>
          <Text style={styles.detailText}>{`Name: ${levelData?.level_name}`}</Text>
          <Text style={styles.detailTextFun}>{`Difficulty: `}</Text>
          <DifficultyDistributionGraph difficultyDistribution={levelData.statement_difficulty_distribution}/>
          
          <Text style={styles.detailTextFun}>{`Duration: ${level?.duration} minutes`}</Text>
          <Text style={styles.detailText}>{`Minimum Score to Pass: ${levelData?.min_score}`}</Text>
          <Text style={styles.detailText}>{`HighScore: ${level?.highscore}`}</Text>

          <View style={styles.buttonContainer}>
            <Button title="Close" onPress={onClose} style={styles.button} />
            <Button title={"Play Again"} onPress={onStart} style={[styles.button, styles.playAgainButton]} />
            
          </View>
        </View>
      </View>
    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  gradient: {
    flex: 1,
    justifyContent: 'center',
  },
  container: {
    width: '100%',
    alignItems: 'center',
  },
  modal: {
    width: '80%',
    backgroundColor: 'rgba(0, 0, 50, 0.9)',
    borderRadius: 10,
    padding: 20,
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 10,
  },
  detailText: {
    fontSize: 16,
    color: 'white',
    marginBottom: 10,
  },
  detailTextFun: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'lightblue',
    marginBottom: 10,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  button: {
    flex: 1,
    marginTop: 10,
  },
  playAgainButton: {
    marginLeft: 10,
  },
});

export default LevelDetails;
