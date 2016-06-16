import docker

cli = docker.Client()


class Container():
    """

    """
    def __init__(self, name):
        """

        :param name:
        :return:
        """
        self.name = name

    def create(self):
        """
        docker run -d --name ________ _________
        :return:
        """
        self.id = cli.create_container(image=self.name)
        return self.id


def ps():
    """

    :return: list of container dictionaries
    """
    return cli.containers()