// import React, { useEffect, useState,useRef } from 'react';
// import { View, Text, StyleSheet, Animated, Button, TouchableOpacity } from 'react-native';
// import { Swipeable } from 'react-native-gesture-handler';
// import { Ionicons } from '@expo/vector-icons';
//
//
// const StatementScreen = ({ statement, onWrongAnswer, onCorrectAnswer,onLast,isLast }) => {
//   const [showSolution, setShowSolution] = useState(false);
//   const [swipeActionPerformed, setSwipeActionPerformed] = useState(false);
//   const [refreshFlag, setRefreshFlag] = useState(false);
//   const [counter,setCounter] = useState(0);
//   const swipeableRef = useRef(null);
//   const translateX = new Animated.Value(0);
//   const answer = statement.right_answer_index;
//   const swipe_right = 'SWIPE_RIGHT';
//   const swipe_left = 'SWIPE_LEFT';
//   const forceRefresh = () => {
//     // Update the state variable to trigger a re-render
//     setRefreshFlag(prevFlag => !prevFlag);
//   };
//   useEffect(() => {
//     setSwipeActionPerformed(false);
//   }, []);
//
//
//   const handleAnswer = (gestureName) => {
//     if(answer === 0){
//       if(gestureName ===swipe_left){
//           onCorrectAnswer()
//       }else{
//           onWrongAnswer()
//       }
//   }else{
//       if(gestureName ===swipe_right){
//           onCorrectAnswer()
//       }else{
//           onWrongAnswer()
//       }
//   }
//   if (isLast){
//       onLast()
//   }
//   }
//   const onSwipeableWillOpen = () => {
//     // Handle any actions before the swipeable opens
//     // For example, reset translations here
//     Animated.timing(translateX, {
//       toValue: 0,
//       duration: 300, // Adjust the duration as needed
//       useNativeDriver: true,
//     }).start();
//   };
//   const handleSwipe = (gestureName) => {
//     if (!swipeActionPerformed) {
//       handleAnswer(gestureName);
//       setSwipeActionPerformed(true);
//       forceRefresh()
//     }
//
//
//     // Reset showSolution after a delay (you can adjust the delay as needed)
//     // setTimeout(() => {
//     //   setShowSolution(false);
//     // }, 1000);
//   };
//
//   const renderLeftActions = (progress, dragX) => {
//     const dragx = Number.parseInt(JSON.stringify(dragX));
//     const prog = Number.parseInt(JSON.stringify(progress));
//
//     if (dragx < 0){
//         // handleSwipe(swipe_left);
//         console.log("\nLEFT\n")
//         handleSwipe(swipe_left)
//     }
//
//
//     const scale = dragX.interpolate({
//       inputRange: [0, 100],
//       outputRange: [0, 1],
//       extrapolate: 'clamp',
//     });
//
//     return (
//       <View style={styles.leftActions}>
//         <Animated.Text style={{ transform: [{ scale }] }}></Animated.Text>
//       </View>
//     );
//   };
//
//   const renderRightActions = (progress, dragX) => {
//     const dragx = Number.parseInt(JSON.stringify(dragX));
//     const prog = Number.parseInt(JSON.stringify(progress));
//
//
//     console.log(dragx)
//     if (dragx > 150){
//       handleSwipe(swipe_right)
//         console.log("RIGHT")
//     }
//
//     const scale = dragX.interpolate({
//       inputRange: [-100, 50],
//       outputRange: [1, 0],
//       extrapolate: 'clamp',
//
//     });
//
//     return (
//       <View style={styles.rightActions}>
//         <Animated.Text style={{ transform: [{ scale }] }}></Animated.Text>
//       </View>
//     );
//   };
//   const increment = () => {
//     setCounter(prev=>prev+1);
//   };
//
//   return (
//     <Swipeable
//     ref={swipeableRef}
//     friction={2}
//     leftThreshold={40}
//     rightThreshold={40}
//     style={{flex:1}}
//     onSwipeableWillOpen={onSwipeableWillOpen}
//     containerStyle={{ transform: [{ translateX }] }}
//     // onSwipe={(event) => handleSwipe(event.direction)}
//     renderLeftActions={renderLeftActions}
//     renderRightActions={renderRightActions}
//   >
//     <View style={{backgroundColor:"",height:"100vh",
//
//     backgroundColor: counter % 2 === 0 ? "" : "",
//     transition: "all .5s ease",
//     WebkitTransition: "all .5s ease",
//     MozTransition: "all .5s ease"
//
//     }}>
//
//       <View style={styles.card }>
//         <Text style={styles.statementText}>{showSolution ? statement.solution : statement.statement[0].en}</Text>
//         {showSolution && (
//           <View style={styles.references}>
//             <Text>References:</Text>
//             {statement.references.map((item, index) => (
//               <Text key={index}>{item}</Text>
//             ))}
//           </View>
//         )}
//       </View>
//                 <View style={styles.buttonsContainerContainer}>
//                 <View style={styles.buttonsContainer}>
//                 <TouchableOpacity onPress={() => handleAnswer(swipe_left)}>
//                     <Ionicons name="ios-arrow-back" size={80} color="white" />
//                     </TouchableOpacity>
//                     <TouchableOpacity onPress={() => handleAnswer(swipe_right)}>
//                     <Ionicons name="ios-arrow-forward" size={80} color="white" />
//                     </TouchableOpacity>
//                 </View>
//                 </View>
//
//     </View>
//     </Swipeable>
//   );
// };
//
// const styles = StyleSheet.create({
//   card: {
//     backgroundColor: 'rgba(0, 0, 50, 0.9)',
//     padding: 20,
//     marginTop: 150,
//     borderRadius: 10,
//     elevation: 5,
//     shadowColor: 'black',
//     shadowOffset: { width: 0, height: 2 },
//     shadowOpacity: 0.3,
//     shadowRadius: 3,
//
//   },
//   buttonsContainerContainer:{
//
//   },
//   buttonsContainer:{
//     // flex:1,
//     flexDirection:"row",
//     justifyContent:"space-between",
//     margin:50,
//     // position: 'absolute',
//     // bottom: -20,
//     // left: 150,
//     zIndex: 1,
//
//   },
//   statementText: {
//     fontSize: 18,
//     marginBottom: 10,
//     color:"white"
//   },
//   references: {
//     marginTop: 20,
//   },
//   leftActions: {
//     flex: 1,
//     backgroundColor: '',
//     justifyContent: 'center',
//     alignItems: 'flex-end',
//     paddingRight: 20,
//   },
//   rightActions: {
//     flex: 1,
//     backgroundColor: '',
//     justifyContent: 'center',
//     alignItems: 'flex-start',
//     paddingLeft: 20,
//   },
// });
//
// export default StatementScreen;
