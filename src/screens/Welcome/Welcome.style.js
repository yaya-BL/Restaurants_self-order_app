import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  container: {
    justifyContent: 'center',
    margin: 32
  },
  skipButton: {
    flex: .1
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
    color: '#33333350',
    textAlign: 'right'
  },
  textCenter: {
    textAlign: 'center'
  },
  imageHolder: {
    flex: .4
  },
  image: {
    
  },
  body: {
      flex: .2,
      justifyContent: 'space-evenly'
  },
  footer: {
      flex: .3,
      justifyContent: 'center',
  },
  footerContent: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center'
  },
  title: {
    fontWeight: '700',
    textAlign: 'center',
    fontSize: 22
  },
  rightActions: {
    flexDirection:'row'
  },
  circleButton: {
      height: 45,
      width: 45,
      backgroundColor: '#33CCFF',
      alignSelf: 'center',
      borderRadius: 23,
  },
  actionSpace: {
      width: 10
  },
  altFooter: {
      justifyContent: 'flex-start'
  },
  button: {
    height: 53,
    backgroundColor: '#33CCFF',
    borderRadius: 8,
    marginBottom: 18,
    justifyContent: 'center'
  },
  altButton: {
    backgroundColor: '#33CCFF10'
  },
  buttonText: {
      textAlign: 'center',
      fontWeight: '700',
      fontSize: 16,
      color: '#fff'
  },
  altButtonText: {
      color: '#000'
  }
})
