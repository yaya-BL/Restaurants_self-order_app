import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  container: {
      backgroundColor: '#fff',
      height: '100%'
  },
  menuSliderContainer: {
    height: 382,
    backgroundColor: '#fff',
    borderRadius: 30,
    position: 'relative',
    shadowColor: '#000000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 10,  
    elevation: 50
  },
  authAbsoluteButtonContainer: {
      position: 'absolute',
      bottom: 0,
      width: '100%',
      flexDirection: 'row',
      justifyContent: 'space-evenly'
  },
  authText: {
      fontWeight: '700',
      fontSize: 18,
      lineHeight: 20.7,
      marginBottom: 16,
      color: '#333333',
      textAlign: 'center'
  },
  borderButtom: {
      height: 3,
      width: 134,
      borderRadius: 40,
      backgroundColor: '#33CCFF'
  },
  dishScroll: {
      height: '100%',
      alignItems: 'center',
  },
  dishImage: {
    //   height:193,
    //   width: 193
  },
  imageContainer: {
      textAlignVertical: 'center'
  }
})
