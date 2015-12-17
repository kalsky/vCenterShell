import unittest
from mock import MagicMock
from vCenterShell.commands.CommandExecuterService import CommandExecuterService


class TestCommandExecuterService(unittest.TestCase):
    def test_connect_execute_was_called(self):
        # Arrange
        network_adapter_retriever_command = MagicMock()

        command_executer_service = CommandExecuterService(None, network_adapter_retriever_command, destroy_virtual_machine_command=None)

        # Act
        command_executer_service.connect()

        # Assert
        network_adapter_retriever_command.execute.assert_called_with()

    def test_destroyVirtualMachineCommand(self):
        network_adapter_retriever_command=None
        destroy_virtual_machine_command = MagicMock()
        command_executer_service = CommandExecuterService(None, network_adapter_retriever_command, destroy_virtual_machine_command)

        command_executer_service.destroy()

        destroy_virtual_machine_command.execute.assert_called_with()

