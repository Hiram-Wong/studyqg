Page({
  data: {
    arrList: [],
    cardCur: 0,
    swiperList: [],


    isBindExpert: true,
    modalName: null,
    textareaValue: ''
  },
  
  onLoad:function() {

    var that = this;
    wx.request({
      method: 'GET',
      url: 'http://127.0.0.1/banner',
      success: function(res){
        console.log(res);
        that.setData({
          swiperList: res.data[0]
          
        })
        console.log(that.data.swiperList);
      }
    });
    wx.request({
      method: 'GET',
      url: 'http://127.0.0.1/',
      success: function (res) {
        that.setData({
          res_total: res.data.total
        })
      }
    })
    this.towerSwiper('swiperList');
    // 初始化towerSwiper 传已有的数组名即可
    
  },
  DotStyle(e) {
    this.setData({
      DotStyle: e.detail.value
    })
  },
  // cardSwiper
  cardSwiper(e) {
    this.setData({
      cardCur: e.detail.current
    })
  },
  // towerSwiper
  // 初始化towerSwiper
  towerSwiper(name) {
    let list = this.data[name];
    for (let i = 0; i < list.length; i++) {
      list[i].zIndex = parseInt(list.length / 2) + 1 - Math.abs(i - parseInt(list.length / 2))
      list[i].mLeft = i - parseInt(list.length / 2)
    }
    this.setData({
      swiperList: list
    })
  },
  // towerSwiper触摸开始
  towerStart(e) {
    this.setData({
      towerStart: e.touches[0].pageX
    })
  },
  // towerSwiper计算方向
  towerMove(e) {
    this.setData({
      direction: e.touches[0].pageX - this.data.towerStart > 0 ? 'right' : 'left'
    })
  },
  // towerSwiper计算滚动
  towerEnd(e) {
    let direction = this.data.direction;
    let list = this.data.swiperList;
    if (direction == 'right') {
      let mLeft = list[0].mLeft;
      let zIndex = list[0].zIndex;
      for (let i = 1; i < list.length; i++) {
        list[i - 1].mLeft = list[i].mLeft
        list[i - 1].zIndex = list[i].zIndex
      }
      list[list.length - 1].mLeft = mLeft;
      list[list.length - 1].zIndex = zIndex;
      this.setData({
        swiperList: list
      })
    } else {
      let mLeft = list[list.length - 1].mLeft;
      let zIndex = list[list.length - 1].zIndex;
      for (let i = list.length - 1; i > 0; i--) {
        list[i].mLeft = list[i - 1].mLeft
        list[i].zIndex = list[i - 1].zIndex
      }
      list[0].mLeft = mLeft;
      list[0].zIndex = zIndex;
      this.setData({
        swiperList: list
      })
    }
  },
  numSteps() {
    this.setData({
      num: this.data.num == this.data.numList.length - 1 ? 0 : this.data.num + 1
    })
  },
  textareaInput(e) {
    // console.log(e)
    this.setData({
      textareaValue: e.detail.value
    })
  },
  
  clear() {
    this.setData({
      textareaValue: "",
    });
    console.log(this.data.textareaValue)
  },
  
  search() {
    var that = this;
    var textvalue = this.data.textareaValue;
    if (textvalue.length>=2){
      wx.request({
        method: 'GET',
        url: 'http://127.0.0.1/',
        data: {
          key: this.data.textareaValue
        },
        success: function (res) {
          console.log(res);
          var total = res.data.data.length;
          console.log(total);
          if (total !== 0) {
            that.setData({
              isBindExpert: false
            })
          } else {
            that.showModal('resModal')
            that.setData({
              isBindExpert: true
            })
          };
          that.setData({
            arrList: res.data.data
          })
        }
      })
    }
    else{
      that.showModal('textareaModal')
    }
  },
  showModal:function(e) {
    console.log(e)
    this.setData({
      modalName: e
    })
  },
  hideModal(e) {
    this.setData({
      modalName: null
    })
  },
  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})