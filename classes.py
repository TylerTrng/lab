class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:

        self.__tv_channel: int = Television.MIN_CHANNEL
        self.__tv_volume: int = Television.MIN_VOLUME
        self.tv_status: bool = False

    def power(self) -> None:
        self.tv_status = not self.tv_status

    def channel_up(self) -> None:
        if self.tv_status:
            if self.__tv_channel == Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL
            else:
                self.__tv_channel += 1
        """
        - This method should be used to adjust the TV channel by incrementing its value.

        """

    def channel_down(self) -> None:
        if self.tv_status:
            if self.__tv_channel == Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL
            else:
                self.__tv_channel -= 1
        """
        - This method should be used to adjust the TV channel by decrementing its value.

        """

    def volume_up(self) -> None:
        if self.tv_status:
            if self.__tv_volume == Television.MAX_VOLUME:
                pass
            else:
                self.__tv_volume += 1
        """
        - This method should be used to adjust the TV volume by incrementing its value.

        """

    def volume_down(self) -> None:
        if self.tv_status:
            if self.__tv_volume == Television.MIN_VOLUME:
                pass
            else:
                self.__tv_volume -= 1
        """
        - This method should be used to adjust the TV volume by decrementing its value.

        """

    def __str__(self):
        return f'TV status: Is on = {self.tv_status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}'
