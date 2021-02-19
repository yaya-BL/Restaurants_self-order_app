import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  container: {
    justifyContent: 'center',
    margin: 32,
  },
  title: {
      fontSize: 22,
      fontWeight: '700',
      lineHeight: 25.3,
      color: '#333333'
  },
  description: {
    marginTop: 30,
    marginBottom: 11,
    fontSize: 14,
    color: '#333333',
    fontWeight: '400'
  },
  formContainer: {
      marginTop: 15
  },
  formLabel: {
    fontWeight: '400',
    fontSize: 14,
    color: '#333333',
    lineHeight: 16.1
  },
  footerTextContainer: {
      marginTop: 10
  },
  footerText: {
      textAlign: 'right',
      color: '#33CCFF',
      fontSize: 16,
      fontWeight: '700',
      lineHeight: 18.4
  },
  textForm: {
      height: 53,
      backgroundColor: '#F3F5F8',
      marginTop: 9,
      borderRadius: 8,
      paddingLeft: 25
  },
  actionButton: {
    marginTop: 30,
    height: 53,
    borderRadius: 8,
    backgroundColor: '#33CCFF',
    justifyContent: 'center'
  },
  actionText: {
    color: '#fff',
    fontWeight: '700',
    fontSize: 16,
    lineHeight: 18.4,
    textAlign: 'center'
  }
})
