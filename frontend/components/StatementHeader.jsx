import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Svg, Circle, G, Line } from 'react-native-svg';

const StatementHeader = ({ level, levelData, currentStatementIndex, score, onTimerExpired }) => {
  const [timer, setTimer] = useState(60);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setTimer((prevTimer) => {
        if (prevTimer === 0) {
          clearInterval(intervalId);
          onTimerExpired();
        }
        return prevTimer > 0 ? prevTimer - 1 : 0;
      });
    }, 1000);

    return () => clearInterval(intervalId);
  }, [onTimerExpired]);

  const numStatements = levelData.num_statements;
  const progress = currentStatementIndex / numStatements;
  const numFilledStars = Math.round(progress * 5);

  return (
    <View style={styles.headerContainer}>
      <View style={styles.leftContainer}>
        <Text style={styles.levelName}>{levelData.level_name}</Text>
        <Text style={styles.scoreText}>Current Score: {score}</Text>
        <View style={styles.starsContainer}>
          {[...Array(numFilledStars)].map((_, index) => (
            <Ionicons key={index} name="star" size={20} color="gold" style={styles.starIcon} />
          ))}
          {[...Array(5 - numFilledStars)].map((_, index) => (
            <Ionicons key={numFilledStars + index} name="star-outline" size={20} color="gold" style={styles.starIcon} />
          ))}
        </View>
      </View>
      <View style={styles.rightContainer}>
        <Svg height="60" width="60">
          {/* Circle representing the clock */}
          <Circle cx="30" cy="30" r="25" stroke="lightblue" strokeWidth="2" fill="transparent" />
          {/* Line for each second in the timer */}
          {[...Array(60)].map((_, index) => (
            <G key={index} transform={`rotate(${index * 6} 30 30)`}>
              <Line x1="30" y1="5" x2="30" y2="10" stroke="lightblue" strokeWidth="2" />
            </G>
          ))}
          {/* Arc representing the timer progress */}
          <Circle
            cx="30"
            cy="30"
            r="28"
            stroke="darkblue"
            strokeWidth="4"
            fill="transparent"
            strokeDasharray={[Math.PI * 56, Math.PI * 56]}
            strokeDashoffset={(Math.PI * 56) * (1 - timer / 60)}
          />
          {/* Text displaying the remaining time in the center */}
          
          <Text style={styles.timerText}>{timer}</Text>
        </Svg>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  headerContainer: {
    marginTop:20,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: 'darkblue',
    padding: 10,
    marginBottom: 10,
    borderRadius: 8,
  },
  leftContainer: {
    flex: 1,
  },
  rightContainer: {
    alignItems: 'center',
  },
  levelName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'lightblue',
  },
  scoreText: {
    fontSize: 16,
    color: 'lightblue',
    marginBottom: 5,
  },
  starsContainer: {
    flexDirection: 'row',
  },
  starIcon: {
    marginHorizontal: 2,
  },
  timerText: {
    marginTop:20,
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: [{ translateX: -8 }, { translateY: -7 }],
    fontSize: 16,
    color: 'lightblue',
  },
});

export default StatementHeader;
