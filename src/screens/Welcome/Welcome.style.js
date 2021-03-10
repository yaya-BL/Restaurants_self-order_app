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
    color: '#33333370',
    textAlign: 'right'
  },
  textCenter: {
    textAlign: 'center'
  },
  imageHolder: {
    flex: .4,
    alignItems:'center'
  },
  image: {
    
  },
  body: {
      flex: .2,
      justifyContent: 'space-evenly'
  },
  footer: {
      flex: .3,
  },
  footerContent: {
    justifyContent: 'space-between',
    alignItems: 'center'
  },
  footerContent2: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent:'space-evenly'
  },
  title: {
    fontWeight: '700',
    textAlign: 'center',
    fontSize: 22
  },
  rightActions: {
    flexDirection:'row',
    justifyContent:'space-between'
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
    width: 156,
    backgroundColor: '#F27621',
    borderRadius: 8,
    marginLeft: 14,
    marginBottom: 18,
    justifyContent: 'center'
  },
  altButton: {
    backgroundColor: '#F7A305'
  },
  buttonText: {
      textAlign: 'center',
      fontWeight: '700',
      fontSize: 16,
      color: '#fff'
  },
  altButtonText: {
      color: '#000'
  },
  buttonStyle: {
    width:156, 
    height:51, 
    borderRadius:5, 
    backgroundColor:'#F27621', 
    marginTop:81, 
    justifyContent:'center'
  },
  buttonTextStyle: {
    textAlign:'center',
    fontSize:16,
    color:'#fff'
  }
})
