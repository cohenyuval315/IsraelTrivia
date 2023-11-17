import React from 'react';
import { View, Text, Modal, StyleSheet, TouchableOpacity } from 'react-native';
import LottieView from 'lottie-react-native';

const ConfettiComponent = () => {
    return (
      <View>
        <LottieView
          source={require('./confetti.json')}
          autoPlay
          loop
        />
      </View>
    );
  };

const FinishScreen = ({ score, level, levelData, onClose }) => {
    
  const pressOk = () => {
    onClose();
  };

  return (
    <Modal transparent={true} animationType="slide" visible={true}>
        <ConfettiComponent/>
      <View style={styles.modalContainer}>
        <View style={styles.modalContent}>
          <Text style={styles.levelName}>{levelData.level_name}</Text>

          <Text style={styles.scoreText}>Your Score:</Text>
          <Text style={styles.bigScoreText}>{score}</Text>

          {level && level.highscore && (
            <Text style={styles.highscoreText}>Your Last Score is {level.highscore}</Text>
          )}
            <Text style={styles.highscoreText}>Min Score To Pass {levelData.min_score}</Text>
          {score > levelData.min_score ? (
            <Text style={styles.passedText}>Passed! The next level is unlocked!</Text>
          ) : (
            <Text style={styles.failText}>Fail... Please Try Again</Text>
          )}

          <TouchableOpacity onPress={pressOk} style={styles.okButton}>
            <Text style={styles.okButtonText}>OK</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modalContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
  modalContent: {
    backgroundColor: '#253448', // Dark bluish color
    padding: 20,
    borderRadius: 10,
    alignItems: 'center',
  },
  levelName: {
    color: 'white',
    fontSize: 24,
    marginBottom: 10,
  },
  scoreText: {
    color: 'white',
    fontSize: 18,
    marginBottom: 5,
  },
  bigScoreText: {
    color: '#43B0F1', // Light blue color
    fontSize: 36,
    fontWeight: 'bold',
    marginBottom: 15,
  },
  highscoreText: {
    color: 'white',
    fontSize: 16,
    marginBottom: 10,
  },
  passedText: {
    color: 'green',
    fontSize: 18,
    marginBottom: 10,
  },
  failText: {
    color: 'red',
    fontSize: 18,
    marginBottom: 10,
  },
  okButton: {
    backgroundColor: '#43B0F1', // Light blue color
    padding: 10,
    borderRadius: 5,
    marginTop: 10,
  },
  okButtonText: {
    color: 'white',
    fontSize: 16,
  },
});

export default FinishScreen;
